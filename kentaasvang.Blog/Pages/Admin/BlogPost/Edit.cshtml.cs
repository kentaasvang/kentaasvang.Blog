using kentaasvang.Blog.Entities;
using kentaasvang.Blog.Repositories;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.RazorPages;

namespace kentaasvang.Blog.Pages.Admin.BlogPost;

public class EditPageModel : PageModel
{
    public BlogPostEntity? BlogPost { get; set; }
    
    private readonly BlogPostRepository _blogPostRepository;

    public EditPageModel(BlogPostRepository blogPostRepository)
    {
        _blogPostRepository = blogPostRepository;
    }
    
    public void OnGet([FromQuery] int id)
    {
        BlogPost = _blogPostRepository.GetById(id);          
    }
    
    public IActionResult OnPost([FromForm] BlogPostEntity blogPost)
    {
        _blogPostRepository.Update(blogPost);
        return RedirectToPage("/Admin/BlogPosts");
    }
}