using Microsoft.AspNetCore.Mvc;
using dotnet.Models;
using dotnet.DataAccessLayer;
using Microsoft.EntityFrameworkCore;
namespace dotnet.Controllers;

[ApiController]
[Route("[controller]")]
public class MemberController : ControllerBase
{
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

    [HttpPost]
    public async Task<IActionResult> PostAsync(Member member)
    {
        _gatherSyncContext.Members.Add(member);
        await _gatherSyncContext.SaveChangesAsync();
        return Created($"{member.Id}", member);
    }

    [HttpPut]
    public async Task<IActionResult> PutAsync(Member memberToUpdate)
    {
        _gatherSyncContext.Members.Update(memberToUpdate);
        await _gatherSyncContext.SaveChangesAsync();
        return NoContent();
    }

    [Route("{id}")]
    [HttpDelete]
    public async Task<IActionResult> DeleteAsync(int id)
    {
        var memberToDelete = await _gatherSyncContext.Members.FindAsync(id);
        if (memberToDelete == null)
        {
            return NotFound();
        }
        _gatherSyncContext.Members.Remove(memberToDelete);
        await _gatherSyncContext.SaveChangesAsync();
        return NoContent();
    }
}
