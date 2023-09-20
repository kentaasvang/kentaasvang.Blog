using Bogus;
using kentaasvang.Blog.Data;
using kentaasvang.Blog.Entities;

namespace kentaasvang.Blog.Seeder;

public class Seeder
{
    public static void Run(ApplicationDbContext context)
    {
        if (context.BlogPosts.Any()) return;
        
        var faker = new Faker<BlogPostEntity>()
            .StrictMode(true)
            .Ignore(p => p.Id) // automatically generated
            .RuleFor(p => p.Title, f => f.Lorem.Sentence())
            .RuleFor(p => p.Content, f => f.Lorem.Paragraphs(f.Random.Int(5, 100)))
            .RuleFor(p => p.Created, f => f.Date.Past())
            .RuleFor(p => p.Updated, f => f.Date.Past())
            .RuleFor(p => p.Published, f => f.Date.Past())
            .RuleFor(p => p.IsPublished, f => f.Random.Bool());

        var blogPosts = faker.Generate(100);

        context.AddRange(blogPosts);
        context.SaveChanges();
    }
}