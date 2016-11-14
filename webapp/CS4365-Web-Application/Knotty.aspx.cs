using System;
using System.Diagnostics;
using System.IO;
using System.Linq;
using Microsoft.Ajax.Utilities;

public partial class Knotty : System.Web.UI.Page
{
    private readonly string pythonPath = @"C:\Python27\python.exe";
    private readonly string enginePath = @"C:\inetpub\wwwroot\engine.exe";
    private readonly string demoPath = @"C:\Python27\examples\demo.kn";
    private readonly string scriptsPath = @"C:\inetpub\wwwroot\Queries\";

    protected void Page_Load(object sender, EventArgs e)
    {
        if (Request.QueryString["scriptId"] != null)
        {
            var file = scriptsPath + Request.QueryString["scriptId"];

            if (!File.Exists(file)) return;

            txtInput.Text = string.Empty;
            foreach (var lineRead in File.ReadAllLines(file))
                txtInput.Text += lineRead + "\n";
            //Request.QueryString["scriptId"] = null;
        }

        lblRecent.Text = string.Empty;
        foreach (var file in Directory.GetFiles(scriptsPath, "*.kn").Select(x => new FileInfo(x)).OrderByDescending(x => x.LastWriteTime).Take(30))
            if (!file.Name.Contains("simplified"))
                lblRecent.Text += $"<a href=\"?scriptId={file.Name}\">{file.Name}</a><br>";        
    }

    protected void SubmitClick(object sender, EventArgs e)
    {
        var file = SaveInputToFile();

        var pInfo = new ProcessStartInfo
        {
            FileName = enginePath,
            Arguments = file
        };

        var p = new Process { StartInfo = pInfo };

        p.Start();
        p.WaitForExit();

        lblOutput.Text = string.Empty;
        try
        {
            foreach (var lineRead in File.ReadAllLines(file.Replace(".kn", ".tex")))
                lblOutput.Text += lineRead + "<br>";
        }
        catch
        {
            lblOutput.Text = "Error! Cannot find file '" + file.Replace(".kn", ".tex").Substring(file.LastIndexOf('\\') + 1) + "'";
        }
    }

    protected void TestClick(object sender, EventArgs e)
    {
        lblOutput.Text = "Beginning Tests...<br>";

        if (!TestFiles())
            return;

        if (!TestLoadDemoFile())
            return;
        
        lblOutput.Text += "Starting external Python process...<br><br>Results:<br>=========================<br>";

        var pInfo = new ProcessStartInfo
        {
            FileName = enginePath,
            Arguments = $"{demoPath}"
        };

        var p = new Process { StartInfo = pInfo };

        p.Start();

        foreach (var lineRead in File.ReadAllLines(demoPath))
            lblOutput.Text += lineRead + "<br>";

        lblOutput.Text += "=========================<br>Testing finished, all tests successful.";
    }

    private bool TestFiles()
    {
        lblOutput.Text += "Locating files...<br>";

        if (!File.Exists(pythonPath))
        {
            lblOutput.Text += "Error, cannot find Python executable in " + pythonPath;
            return false;
        }
        lblOutput.Text += "Found Python executable... (1/3)<br>";

        if (!File.Exists(enginePath))
        {
            lblOutput.Text += "Error, cannot find Knotty engine in " + enginePath;
            return false;
        }
        lblOutput.Text += "Found Knotty engine... (2/3)<br>";

        if (!File.Exists(demoPath))
        {
            lblOutput.Text += "Error, cannot find Knotty demo file in " + enginePath;
            return false;
        }
        lblOutput.Text += "Found Knotty demo file... (3/3)<br>All files found.<br>";

        return true;
    }

    private bool TestLoadDemoFile()
    {
        try
        {
            lblOutput.Text += "Loading demo file...<br>";

            txtInput.Text = string.Empty;

            foreach (var lineRead in File.ReadAllLines(demoPath))
                txtInput.Text += lineRead + "\n";

            lblOutput.Text += "Demo file loaded...<br>";
        }
        catch (Exception)
        {
            lblOutput.Text = "Error, something went wrong in TestLoadDemoFile()!";
            return false;
        }

        return true;
    }

    private string SaveInputToFile()
    {
        var file = scriptsPath + (!txtName.Text.IsNullOrWhiteSpace() ? txtName.Text + '_' : string.Empty) + DateTime.UtcNow.ToFileTime() + ".kn";
        File.WriteAllText(file, txtInput.Text);
        return file;
    }
}