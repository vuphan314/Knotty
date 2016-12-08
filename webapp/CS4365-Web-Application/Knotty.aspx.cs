using System;
using System.Diagnostics;
using System.IO;
using System.IO.Compression;
using System.Linq;
using Microsoft.Ajax.Utilities;

public partial class Knotty : System.Web.UI.Page
{
    private readonly string enginePath = @"C:\inetpub\wwwroot\knotty.exe";
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
        lblRecentDl.Text = string.Empty;

        foreach (
            var file in
                Directory.GetFiles(scriptsPath, "*.kn")
                    .Select(x => new FileInfo(x))
                    .OrderByDescending(x => x.LastWriteTime)
                    .Take(30))
        {
            lblRecent.Text += $"<a href=\"?scriptId={file.Name}\">{file.Name}</a><br>";
            var tex = file.Name.Replace(".kn", ".tex");
            var zip = file.Name.Replace(".kn", ".zip");
            if (File.Exists(scriptsPath + tex))
            {
                lblRecentDl.Text += $"<a href=\"Queries/{tex}\">.tex</a>";
                if (File.Exists(scriptsPath + zip))
                    lblRecentDl.Text += $" | <a href=\"Queries/{zip}\">.kn + .tex</a><br>";
                else
                    lblRecentDl.Text += "<br>";
            }
            else if (File.Exists(scriptsPath + zip))
                lblRecentDl.Text += $"<a href=\"Queries/{zip}\">.kn + .tex</a><br>";
        }

        if (IsPostBack)
            txtOutput.Focus(); 
    }

    protected void SubmitClick(object sender, EventArgs e)
    {
        var knFile = SaveInputToFile();
        var texFile = knFile.Replace(".kn", ".tex");

        var pInfo = new ProcessStartInfo
        {
            FileName = enginePath,
            Arguments = knFile
        };

        var p = new Process { StartInfo = pInfo };

        p.Start();
        p.WaitForExit();

        using (ZipArchive zip = ZipFile.Open(knFile.Replace(".kn", ".zip"), ZipArchiveMode.Create))
        {
            zip.CreateEntryFromFile(knFile, knFile, CompressionLevel.Fastest);
            zip.CreateEntryFromFile(texFile, texFile, CompressionLevel.Fastest);
        }

        txtOutput.Text = string.Empty;
        try
        {
            txtOutput.Text = File.ReadAllText(texFile);
            //foreach (var lineRead in File.ReadAllLines(file.Replace(".kn", ".tex")))
            //    txtOutput.Text += lineRead + "<br>";
        }
        catch
        {
            txtOutput.Text = "Error! Cannot find file '" + knFile.Replace(".kn", ".tex").Substring(knFile.LastIndexOf('\\') + 1) + "'";
        }
    }

    protected void TestClick(object sender, EventArgs e)
    {
        txtOutput.Text = "Beginning Tests...<br>";

        if (!TestFiles())
            return;

        if (!TestLoadDemoFile())
            return;
        
        txtOutput.Text += "Starting external Python process...<br><br>Results:<br>=========================<br>";

        var pInfo = new ProcessStartInfo
        {
            FileName = enginePath,
            Arguments = $"{demoPath}"
        };

        var p = new Process { StartInfo = pInfo };

        p.Start();

        foreach (var lineRead in File.ReadAllLines(demoPath))
            txtOutput.Text += lineRead + "<br>";

        txtOutput.Text += "=========================<br>Testing finished, all tests successful.";
    }

    private bool TestFiles()
    {
        txtOutput.Text += "Locating files...<br>";

        if (!File.Exists(enginePath))
        {
            txtOutput.Text += "Error, cannot find Knotty engine in " + enginePath;
            return false;
        }
        txtOutput.Text += "Found Knotty engine... (1/2)<br>";

        if (!File.Exists(demoPath))
        {
            txtOutput.Text += "Error, cannot find Knotty demo file in " + enginePath;
            return false;
        }
        txtOutput.Text += "Found Knotty demo file... (2/2)<br>All files found.<br>";

        return true;
    }

    private bool TestLoadDemoFile()
    {
        try
        {
            txtOutput.Text += "Loading demo file...<br>";

            txtInput.Text = string.Empty;

            foreach (var lineRead in File.ReadAllLines(demoPath))
                txtInput.Text += lineRead + "\n";

            txtOutput.Text += "Demo file loaded...<br>";
        }
        catch (Exception)
        {
            txtOutput.Text = "Error, something went wrong in TestLoadDemoFile()!";
            return false;
        }

        return true;
    }

    private string SaveInputToFile()
    {
        var file = scriptsPath + (!txtName.Text.IsNullOrWhiteSpace() ? txtName.Text.Replace(' ','_') + '_' : string.Empty) + DateTime.UtcNow.ToFileTime() + ".kn";
        File.WriteAllText(file, txtInput.Text);
        return file;
    }

    protected void Clear_OnClick(object sender, EventArgs e)
    {
        Response.Redirect(Request.Url.GetLeftPart(UriPartial.Path));
    }
}