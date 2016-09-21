using Microsoft.Owin;
using Owin;

[assembly: OwinStartupAttribute(typeof(CS4365.Startup))]
namespace CS4365
{
    public partial class Startup {
        public void Configuration(IAppBuilder app) {
            ConfigureAuth(app);
        }
    }
}
