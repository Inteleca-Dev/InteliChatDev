<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="SignIn.aspx.cs" Inherits="SharePointSignInPage.SignIn" %>
<!DOCTYPE html>
<html>
<head>
    <title>Sign In</title>
    <style>
        /* Add your custom CSS styles here */
    </style>
</head>
<body>
    <form id="form1" runat="server">
        <div>
            <h2>Sign In</h2>
            <asp:Label ID="lblErrorMessage" runat="server" ForeColor="Red"></asp:Label>
            <br /><br />
            <asp:TextBox ID="txtUsername" runat="server" placeholder="Username"></asp:TextBox>
            <br /><br />
            <asp:TextBox ID="txtPassword" runat="server" TextMode="Password" placeholder="Password"></asp:TextBox>
            <br /><br />
            <asp:Button ID="btnSignIn" runat="server" Text="Sign In" OnClick="btnSignIn_Click" />
        </div>
    </form>
</body>
</html>