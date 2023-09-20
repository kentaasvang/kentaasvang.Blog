using kentaasvang.Blog;
using kentaasvang.Blog.Data;
using kentaasvang.Blog.Seeder;
using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.DependencyInjection;

var configurationBuilder = new ConfigurationBuilder()
    .SetBasePath(Path.Combine(AppContext.BaseDirectory, "../../../../kentaasvang.Blog"))
    .AddJsonFile("appsettings.Development.json");

var configuration = configurationBuilder.Build();

var services = new ServiceCollection();
services.AddDatabase(configuration);

using var serviceProvider = services.BuildServiceProvider();
var dbContext = serviceProvider.GetRequiredService<ApplicationDbContext>();

Seeder.Run(dbContext);

Console.WriteLine("Done seeding database.");