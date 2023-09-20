namespace kentaasvang.Blog.Entities;

public class BlogPostEntity
{
    public int Id { get; set; }
    public string? Title { get; set; }
    public string? Content { get; set; }
    public DateTime Created { get; set; }
    public DateTime Updated { get; set; }
    public DateTime Published { get; set; }
    public bool IsPublished { get; set; }
}