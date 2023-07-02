// using dotnet.Models;
// using System.Data.Entity.Design;
// using System.Data.Entity.ModelConfiguration.Conventions;

// namespace dotnet.DataAccessLayer
// {
//     public class GatherSyncContext : DbContext
//     {
    
//         public GatherSyncContext() : base("GatherSyncContext")
//         {
//         }
        
//         public DbSet<Member> Members { get; set; }
    
//         protected override void OnModelCreating(DbModelBuilder modelBuilder)
//         {
//             modelBuilder.Conventions.Remove<PluralizingTableNameConvention>();
//         }
//     }
// }