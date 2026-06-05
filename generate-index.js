const fs = require("fs");
const path = require("path");

const root = process.cwd();

const excludedDirs = new Set([
  ".git",
  ".github",
  "node_modules",
  "dist",
  "build"
]);

const dirs = fs.readdirSync(root, { withFileTypes: true })
  .filter(entry => entry.isDirectory())
  .map(entry => entry.name)
  .filter(name => !excludedDirs.has(name))
  .filter(name => fs.existsSync(path.join(root, name, "index.html")))
  .sort();

const links = dirs
  .map(dir => `<li><a href="./${dir}/">${dir}</a></li>`)
  .join("\n");

const repoName = process.env.GITHUB_REPOSITORY
  ? process.env.GITHUB_REPOSITORY.split("/")[1]
  : "Projects";

const html = `<!doctype html>
<html lang="nl">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>${repoName}</title>
  <style>
    body {
      font-family: system-ui, sans-serif;
      max-width: 720px;
      margin: 40px auto;
      padding: 0 20px;
      line-height: 1.5;
    }

    li {
      margin: 0.4rem 0;
    }
  </style>
</head>
<body>
  <h1>${repoName}</h1>
  <ul>
    ${links}
  </ul>
</body>
</html>
`;

fs.writeFileSync(path.join(root, "index.html"), html);
console.log(`Generated index.html with ${dirs.length} links.`);