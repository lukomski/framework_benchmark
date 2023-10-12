using dotnet.Models;
using Microsoft.EntityFrameworkCore;

namespace dotnet.DataAccessLayer
{
    public class GatherSyncContext : DbContext
    {

        // Uncomment this for non-docker running
        // private string ConnectionString = "Server=localhost;Database=fwbm;Port=5435;User Id=postgres;Integrated Security=True;";
        
        // Uncomment this for docker running
        private string ConnectionString = "Server=db;Database=fwbm;Port=5432;User Id=postgres;Integrated Security=True;";

        public GatherSyncContext()
        {
        }

        protected override void OnConfiguring(DbContextOptionsBuilder options)
                => options.UseNpgsql(ConnectionString);

        public DbSet<Member> Members { get; set; }
    }
}