# check for argument
if [ $# -eq 0 ]
  then
    read -p "Enter migration name: " migrationName
else
  migrationName=$1
fi

dotnet ef migrations add $migrationName --project kentaasvang.CMS --output-dir Data/Migrations
