using Microsoft.AspNetCore.Mvc.RazorPages;

namespace kentaasvang.Blog.Pages;

public class PostModel : PageModel
{
    public string? BlogPost { get; set; }
    
    public void OnGet()
    {
        var content = System.IO.File.ReadAllText("wwwroot/posts/post1.md");        
        BlogPost = Markdig.Markdown.ToHtml(content);          
    }
}