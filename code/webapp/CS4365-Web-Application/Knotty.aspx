<%@ Page Language="C#" AutoEventWireup="true" CodeFile="Knotty.aspx.cs" Inherits="Knotty" %>

<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <title></title>
</head>
<body>
    <form id="form1" runat="server">
    <div>
        <asp:Table runat="server" Width="75%" HorizontalAlign="Center" Font-Names="Calibri" CellSpacing="5">
            <asp:TableRow runat="server">
                <asp:TableCell runat="server" Font-Size="24" HorizontalAlign="Center" ColumnSpan="4">Knotty</asp:TableCell>
            </asp:TableRow>
            <asp:TableRow runat="server">
                <asp:TableCell runat="server" Font-Size="18" HorizontalAlign="Center" ColumnSpan="4">a computer algebra system designed for knot theory</asp:TableCell>
            </asp:TableRow>
            <asp:TableRow runat="server">
                <asp:TableCell runat="server"></asp:TableCell>
                <asp:TableCell runat="server">Input:</asp:TableCell>
                <asp:TableCell runat="server">Output:</asp:TableCell>
                <asp:TableCell runat="server">Recent:</asp:TableCell>
            </asp:TableRow>
            <asp:TableRow runat="server">
                <asp:TableCell runat="server" Width="10%"></asp:TableCell>
                <asp:TableCell runat="server" Width="40%"><asp:TextBox ID="txtInput" runat="server" Height="600px" Width="90%" TextMode="MultiLine"></asp:TextBox></asp:TableCell>
                <asp:TableCell runat="server" Width="40%" VerticalAlign="Top"><asp:Label runat="server" ID="lblOutput"></asp:Label></asp:TableCell>
                <asp:TableCell runat="server" Width="10%" ID="recentFiles" VerticalAlign="Top"></asp:TableCell>
            </asp:TableRow>
            <asp:TableRow runat="server">
                <asp:TableCell runat="server"></asp:TableCell>
                <asp:TableCell runat="server"></asp:TableCell>
                <asp:TableCell runat="server" HorizontalAlign="Right"><asp:Button runat="server" Text="Submit" OnClick="SubmitClick"/>&nbsp;&nbsp;<asp:Button runat="server" Text="Run Tests" OnClick="TestClick"/></asp:TableCell>
                <asp:TableCell runat="server"></asp:TableCell>
            </asp:TableRow>
        </asp:Table>
    </div>
    </form>
</body>
</html>
