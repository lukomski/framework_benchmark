using System.ComponentModel.DataAnnotations;

namespace dotnet.Models;

public class Member
{
    public int Id { get; set; }
    public string Name { get; set; }

    public Member(string name) {
        Name = name;
    }
}
