using kentaasvang.Blog.Entities;
using kentaasvang.Blog.Repositories;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.RazorPages;

namespace kentaasvang.Blog.Pages;

public class BlogPostPageModel : PageModel
{
    public BlogPostEntity? BlogPost { get; set; }
    
    private readonly BlogPostRepository _blogPostRepository;

    public BlogPostPageModel(BlogPostRepository blogPostRepository)
    {
        _blogPostRepository = blogPostRepository;
    }
    
    public void OnGet([FromQuery] int id)
    {
        // var content = System.IO.File.ReadAllText("wwwroot/posts/post1.md");        
        // BlogPost = Markdig.Markdown.ToHtml(content);          
        BlogPost = _blogPostRepository.GetById(id);
    }
}