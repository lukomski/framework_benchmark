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

    [Route("clear")]
    [HttpPost]
    public async Task<IActionResult> PostClearAsync()
    {
        _gatherSyncContext.Members.RemoveRange(_gatherSyncContext.Members);
         await _gatherSyncContext.SaveChangesAsync();
        return Ok($"Count of Members: {_gatherSyncContext.Members.Count()}");
    }

    [Route("fill-in")]
    [HttpPost]
    public async Task<IActionResult> PostFillInAsync()
    {
        for (int index = 0; index < 1000; index++)
        {
            var member = new Member($"Name {index}");
            _gatherSyncContext.Members.Add(member);
        }       
        await _gatherSyncContext.SaveChangesAsync();
        return Ok($"Count of Members: {_gatherSyncContext.Members.Count()}");
    }
}
