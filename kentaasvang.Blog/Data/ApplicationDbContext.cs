using kentaasvang.Blog.Entities;
using Microsoft.EntityFrameworkCore;

namespace kentaasvang.Blog.Data;

public class ApplicationDbContext : DbContext
{
    public DbSet<BlogPostEntity> BlogPosts => Set<BlogPostEntity>();
    
    public ApplicationDbContext(DbContextOptions<ApplicationDbContext> options) : base(options)
    {
    }
}