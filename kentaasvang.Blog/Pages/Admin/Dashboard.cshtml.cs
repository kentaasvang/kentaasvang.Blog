using kentaasvang.Blog.Entities;
using kentaasvang.Blog.Repositories;
using Microsoft.AspNetCore.Mvc.RazorPages;

namespace kentaasvang.Blog.Pages.Admin;

public class DashboardPageModel : PageModel
{
    public List<BlogPostEntity>? BlogPosts { get; set; }
    
    private readonly BlogPostRepository _blogPostRepository;

    public DashboardPageModel(BlogPostRepository blogPostRepository)
    {
        _blogPostRepository = blogPostRepository;
    }
    
    public void OnGet()
    {
        BlogPosts = _blogPostRepository.GetAll();
    }
}