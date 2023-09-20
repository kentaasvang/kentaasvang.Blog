using kentaasvang.Blog.Data;
using kentaasvang.Blog.Entities;
using Microsoft.EntityFrameworkCore;

namespace kentaasvang.Blog.Repositories;

public class BlogPostRepository
{
    private readonly ApplicationDbContext _applicationDbContext;

    public BlogPostRepository(ApplicationDbContext applicationDbContext)
    {
        _applicationDbContext = applicationDbContext;
    }

    public List<BlogPostEntity> GetAll()
    {
        var blogPostEntities = _applicationDbContext.BlogPosts
            .AsNoTracking()
            .OrderBy(bp => bp.Published)
            .ToList();
        
        return blogPostEntities;
    }
    
    public BlogPostEntity? GetById(int id)
    {
        var blogPostEntity = _applicationDbContext.BlogPosts
            .AsNoTracking()
            .FirstOrDefault(bp => bp.Id == id);
        
        return blogPostEntity;
    }
}