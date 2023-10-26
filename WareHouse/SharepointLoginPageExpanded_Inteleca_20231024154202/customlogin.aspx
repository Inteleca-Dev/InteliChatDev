using System;
using System.Web;
using System.Web.UI;
using System.DirectoryServices.AccountManagement;
namespace CustomLoginPage
{
    public partial class CustomLogin : Page
    {
        protected void LoginButton_Click(object sender, EventArgs e)
        {
            string username = Username.Text;
            string password = Password.Text;
            // Implement authentication logic here
            bool isAuthenticated = AuthenticateUser(username, password);
            if (isAuthenticated)
            {
                // Redirect to SharePoint page
                Response.Redirect("https://your-sharepoint-site.com");
            }
            else
            {
                // Display error message
                Response.Write("Invalid username or password");
            }
        }
        private bool AuthenticateUser(string username, string password)
        {
            // Implement authentication against Active Directory or provider
            // Return true if authentication is successful, false otherwise
            // Example:
            using (var context = new PrincipalContext(ContextType.Domain))
            {
                return context.ValidateCredentials(username, password);
            }
        }
    }
}