<%@ Page Language="C#" AutoEventWireup="true" CodeFile="Knotty.aspx.cs" Inherits="Knotty" %>

<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <title>Knotty - a computer algebra system designed for knot theory</title>
</head>
<body>
    <form id="form1" runat="server" DefaultFocus="txtName">
    <div>
        <asp:Table runat="server" Width="75%" Height="90%" HorizontalAlign="Center" Font-Names="Calibri" CellSpacing="5">
            <asp:TableRow runat="server">
                <asp:TableCell runat="server" Font-Size="24" HorizontalAlign="Center" ColumnSpan="3">Knotty</asp:TableCell>
            </asp:TableRow>
            <asp:TableRow runat="server">
                <asp:TableCell runat="server" Font-Size="18" HorizontalAlign="Center" ColumnSpan="3">a computer algebra system designed for knot theory</asp:TableCell>
            </asp:TableRow>
            <asp:TableRow runat="server">
                <asp:TableCell runat="server" Font-Size="12" HorizontalAlign="Center" ColumnSpan="3">
                    <a href="https://github.com/vuphan314/Knotty">github</a> | Author: <a href="https://github.com/vuphan314">Vu Phan</a> | Website: <a href="https://github.com/zgrummons">Zachariah Grummons</a>
                </asp:TableCell>
            </asp:TableRow>
            <asp:TableRow runat="server">
                <asp:TableCell runat="server">Input:</asp:TableCell>
                <asp:TableCell runat="server">Output:</asp:TableCell>
                <asp:TableCell runat="server">Recent:</asp:TableCell>
            </asp:TableRow>
            <asp:TableRow runat="server">
                <asp:TableCell runat="server" Width="40%" Height="5%" VerticalAlign="Top">
                    <asp:TextBox ID="txtName" Width="90%" runat="server" MaxLength="80" placeholder="Query Title (optional)"></asp:TextBox>
                </asp:TableCell>
                <asp:TableCell runat="server" Width="40%" VerticalAlign="Top" RowSpan="2">
                    <asp:TextBox runat="server" ID="txtOutput" TextMode="MultiLine" Width="90%" Height="100%" ReadOnly="True"></asp:TextBox>
                </asp:TableCell>
                <asp:TableCell runat="server" Width="20%" Height="90%" VerticalAlign="Top" RowSpan="2">
                    <asp:Label runat="server" ID="lblRecent"></asp:Label>
                </asp:TableCell>
            </asp:TableRow>
            <asp:TableRow runat="server">     
                <asp:TableCell runat="server">
                    <asp:TextBox ID="txtInput" runat="server" Height="100%" Width="90%" TextMode="MultiLine"></asp:TextBox>
                </asp:TableCell>               
            </asp:TableRow>
            <asp:TableRow runat="server">
                <asp:TableCell runat="server"></asp:TableCell>
                <asp:TableCell runat="server" HorizontalAlign="Right">
                    <asp:Button runat="server" Text="Submit" OnClick="SubmitClick"/>
                    <!-- &nbsp;&nbsp;<asp:Button runat="server" Text="Run Tests" OnClick="TestClick"/> -->
                    <asp:Button runat="server" Text="Clear" OnClick="Clear_OnClick"/>
                </asp:TableCell>
                <asp:TableCell runat="server"></asp:TableCell>
            </asp:TableRow>
        </asp:Table>
    </div>
    </form>
</body>
</html>
