using kentaasvang.Blog.Data;
using Microsoft.EntityFrameworkCore;

namespace kentaasvang.Blog;

public static class CreateServices
{
    public static void AddDatabase(this IServiceCollection services, IConfiguration configuration)
    {
        var connectionString = configuration.GetConnectionString("DefaultConnection");
        var serverVersion = ServerVersion.AutoDetect(connectionString);
        services.AddDbContext<ApplicationDbContext>(options =>
            options.UseMySql(connectionString, serverVersion));
    }
}