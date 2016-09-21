using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.IO;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

public partial class _Default : System.Web.UI.Page
{
    private string pythonPath = @"C:\Python27\python.exe";
    private string enginePath = @"C:\Python27\engine.py";
    private string demoPath = @"C:\Python27\examples\demo.kn";

    protected void Page_Load(object sender, EventArgs e)
    {

    }

    protected void SubmitClick(object sender, EventArgs e)
    {
        //Waiting for a real, working version of the engine

        //var pInfo = new ProcessStartInfo
        //{
        //    FileName = pythonPath,
        //    Arguments = $"{enginePath} {demoPath}"
        //};

        //var p = new Process { StartInfo = pInfo };

        //p.Start();

        //foreach (var lineRead in File.ReadAllLines(demoPath))
        //    lblOutput.Text += lineRead + "<br>";

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
            FileName = pythonPath,
            Arguments = $"{enginePath} {demoPath}"
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
            {
                txtInput.Text += lineRead + "\n";
            }

            lblOutput.Text += "Demo file loaded...<br>";
        }
        catch (Exception)
        {
            lblOutput.Text = "Error, something went wrong in TestLoadDemoFile()!";
            return false;
        }

        return true;
    }
}