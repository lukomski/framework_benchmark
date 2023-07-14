using Microsoft.AspNetCore.Mvc;
using dotnet.Models;
using dotnet.DataAccessLayer;
using Microsoft.EntityFrameworkCore;
namespace dotnet.Controllers;

[ApiController]
[Route("[controller]")]
public class MemberController : ControllerBase
{
    private static readonly string[] Names = new[]
    {
        "Liam",
        "Noah",
        "William",
        "James",
        "Logan",
        "Benjamin",
        "Mason"
    };



    private readonly GatherSyncContext _gatherSyncContext;

    public MemberController(GatherSyncContext gatherSyncContext)
    {
        _gatherSyncContext = gatherSyncContext;
    }

    [HttpGet("")]
    public async Task<IEnumerable<Member>> GetAsync()
    {
        var memebers = await _gatherSyncContext.Members.ToListAsync();
        return memebers;
    }

    [HttpGet("random")]
    public IEnumerable<Member> Get()
    {
        return Enumerable.Range(1, 5).Select(index =>
            new Member(Names[Random.Shared.Next(Names.Length)])
        )
        .ToArray();
    }
}
