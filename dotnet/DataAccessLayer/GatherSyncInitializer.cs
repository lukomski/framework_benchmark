// using System;
// using System.Collections.Generic;
// using System.Linq;
// using System.Web;
// using System.Data.Entity;
// using dotnet.Models;

// namespace dotnet.DataAccessLayer
// {
//     public class GatherSyncInitializer : System.Data.Entity. DropCreateDatabaseIfModelChanges<GatherSyncContext>
//     {
//         protected override void Seed(GatherSyncContext context)
//         {
//             var members = new List<Member>
//             {
//             new Member{Name="Carson"},
//             new Member{Name="Meredith"},
//             new Member{Name="Arturo"},
//             new Member{Name="Gytis"},
//             new Member{Name="Yan"},
//             new Member{Name="Peggy"},
//             new Member{Name="Laura"},
//             new Member{Name="Nino"}
//             };

//             members.ForEach(s => context.Members.Add(s));
//         }
//     }
// }