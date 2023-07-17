using dotnet.Models;
using Microsoft.EntityFrameworkCore;

namespace dotnet.DataAccessLayer
{
    public class GatherSyncContext : DbContext
    {

        private string ConnectionString = "Server=localhost;Database=fwbm;Port=5435;User Id=postgres;Integrated Security=True;";

        public GatherSyncContext()
        {
        }

        protected override void OnConfiguring(DbContextOptionsBuilder options)
                => options.UseNpgsql(ConnectionString);

        public DbSet<Member> Members { get; set; }
    }
}