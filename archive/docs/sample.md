<!-- 
╔══════════════════════════════════════════════════════════════════════════════╗
║                                                                              ║
║   ██████╗ ███████╗██████╗  ██████╗ ██╗   ██╗ █████╗ ███╗   ██╗██╗   ██╗██╗   ║
║   ██╔══██╗██╔════╝██╔══██╗██╔═══██╗╚██╗ ██╔╝██╔══██╗████╗  ██║██║   ██║██║   ║
║   ██████╔╝█████╗  ██║  ██║██║   ██║ ╚████╔╝ ███████║██╔██╗ ██║██║   ██║██║   ║
║   ██╔══██╗██╔══╝  ██║  ██║██║   ██║  ╚██╔╝  ██╔══██║██║╚██╗██║██║   ██║██║   ║
║   ██║  ██║███████╗██████╔╝╚██████╔╝   ██║   ██║  ██║██║ ╚████║╚██████╔╝███████╗
║   ╚═╝  ╚═╝╚══════╝╚═════╝  ╚═════╝    ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚══════╝
║                                                                              ║
║              🚀 AI DEVELOPER • PYTHON ENGINEER • PROBLEM SOLVER 🚀           ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝
-->

<div align="center">
  
  <!-- ═══════════════════════════════════════════════════════════════════════════ -->
  <!-- 🎯 ANIMATED HEADER                                                          -->
  <!-- ═══════════════════════════════════════════════════════════════════════════ -->
  
  <img src="./assets/header-animation.svg" alt="Redoyanul Haque - AI Developer" width="100%"/>
  
  <br/>

</div>

<br/>

<!-- ═══════════════════════════════════════════════════════════════════════════ -->
<!-- 🖥️ TERMINAL INTRO SECTION                                                   -->
<!-- ═══════════════════════════════════════════════════════════════════════════ -->

<div align="center">
  <img src="./assets/terminal-intro.svg" alt="Terminal Introduction" width="650"/>
</div>

<br/>

<img src="./assets/divider.svg" width="100%"/>

<br/>






Description : 

1. The animated header Should have details about me. The above is a sample for referance.

2. "🧱 Breakout	breakout	A ball bounces around breaking your contribution bricks" from generate-pacman-game-from-github-contribution-grid

From - name: generate-pacman-game-from-github-contribution-grid
  uses: abozanona/pacman-contribution-graph@v5.0.0

🧩 Usage
Here's how to set up and run the games:

Include the Library: Ensure the library is included in your project, either via npm or a script tag.

Initialize the Game: Use the following code to generate an arcade game:

import { ArcadeRenderer } from 'pacman-contribution-graph';

// Replace [game-name] with a valid game name
const renderer = new ArcadeRenderer({
	game: '[game-name]',
	username: 'your_username',
	platform: 'github', // or 'gitlab'
	gameTheme: 'github-dark', // 'github', 'github-dark', 'gitlab', or 'gitlab-dark'
	playerStyle: 'opportunistic', // Pac-Man only: 'conservative', 'aggressive', or 'opportunistic'
	svgCallback: (svg) => {
		// called with the generated SVG string
		document.getElementById('output').innerHTML = svg;
	},
	gameOverCallback: () => {
		console.log('Game over!');
	},
	pointsIncreasedCallback: (points) => {
		console.log('Score:', points);
	}
});
renderer.start();
Customize Settings: Adjust the parameters as needed:

game: The arcade game name to generate. For valid names, see table above.
username: Your GitHub or GitLab username.
platform: Specify 'github', 'gitlab' or 'scenario'.
gameTheme: Choose between 'github', 'github-dark', 'gitlab', or 'gitlab-dark'.
scenario: Use a predefined contribution scenario instead of fetching platform contributions. Available scenarios: full, empty, random, checkerboard, gradient, streaks. This option is only active when platform is set to 'scenario'; with platform: 'github' or platform: 'gitlab', real platform contributions are fetched and the scenario value is ignored.
playerStyle (Pac-Man only): PlayerStyle.OPPORTUNISTIC (default), PlayerStyle.CONSERVATIVE, or PlayerStyle.AGGRESSIVE.
svgCallback: Called with the finished SVG string once generation is complete.
gameOverCallback: Called when the game finishes.
pointsIncreasedCallback: Called each time the score increases.
gameStatsCallback: Called at the end with { totalScore, steps, ghostsEaten }.
githubSettings: { accessToken: 'your_token' } for private contribution data.
CLI
Basic
pacman-contribution-graph --game pacman --username demo --platform github --gameTheme github --output pacman-contribution-graph.svg
Use this mode for real contribution data from GitHub or GitLab. --platform and --username are required; --game, --gameTheme, and --output are optional.

Scenario
pacman-contribution-graph --game pacman --username demo --platform scenario --gameTheme github --scenario checkerboard --output pacman-scenario.svg
Use this mode for predefined contribution data, for example demos, screenshots, or local testing. --scenario only works with --platform scenario; if omitted, the CLI uses random. --username is still required by the CLI, but in scenario mode it can be any placeholder value because no user data is fetched.

Integrate into Your GitHub Profile
To showcase the Pac-Man game on your GitHub profile, follow these steps:

Create a Special Repository:

Name a new repository exactly as your GitHub username (e.g., username/username).
This repository powers your GitHub profile page.
Set Up GitHub Actions:

In the repository, create a .github/workflows/ directory.

Add a main.yml file with the following content:

name: generate arcade contribution graphs

on:
    schedule: # Run automatically every 24 hours
        - cron: '0 0 * * *'
    workflow_dispatch: # Allows manual triggering
    push: # Runs on every push to the main branch
        branches:
            - main

jobs:
    generate:
        permissions:
            contents: write
        runs-on: ubuntu-latest
        timeout-minutes: 20

        steps:
            - name: generate contribution graph SVGs
              uses: abozanona/pacman-contribution-graph@main
              with:
                  github_user_name: ${{ github.repository_owner }}
                  # Comma-separated list of game names to generate. Default: pacman
                  games: 'pacman,breakout'

            # Push the generated SVGs to the output branch
            - name: push SVGs to the output branch
              uses: crazy-max/ghaction-github-pages@v3.1.0
              with:
                  target_branch: output
                  build_dir: dist
              env:
                  GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
Add to Profile README:

In your repository, create or edit the README.md file to include. Replace [USERNAME] with your GitHub username and [game-name] with the game (e.g. pacman, breakout, …). Repeat the block for each game you enabled.

## My Contribution Graph

<!-- [game-name] -->
<picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/[USERNAME]/[USERNAME]/output/[game-name]-contribution-graph-dark.svg">
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/[USERNAME]/[USERNAME]/output/[game-name]-contribution-graph.svg">
    <img alt="[game-name] contribution graph" src="https://raw.githubusercontent.com/[USERNAME]/[USERNAME]/output/[game-name]-contribution-graph.svg">
</picture>
Commit and Push:

Push the changes to GitHub. The GitHub Actions workflow will run daily, updating the Pac-Man game on your profile.
For a detailed guide, refer to the blog post: Integrate Pac-Man Contribution Graph into Your GitHub Profile

Integrate into Your GitLab Profile
To showcase the Pac-Man game on your GitLab profile, follow these steps:

Create a Special Repository:

Name a new repository exactly as your GitLab username (e.g., username/username).
This repository powers your GitLab profile page.
Generate & Setup Push Token:

Open the repository, and from left sidebar navigate to settings => Access Token tab.
Generate a new Access Token with the name CI/CD Push Token & scope write_repository. Access tokens are only valid for 1 year maximum.
From left sidebar navigate to settings => CI/CD.
In Variables section, add a new variable with the name CI_PUSH_TOKEN and the value of the Access Token. Make sure that the variable is Masked & Protect.
Set Up gitlab-ci File:

In the repository, create a .gitlab-ci.yml file with the following content. Replace [game-name] with your chosen game. Add one block per game.

stages:
    - generate
    - deploy

variables:
    GIT_SUBMODULE_STRATEGY: recursive

generate_graphs:
    stage: generate
    image: node:20
    script:
        - mkdir -p dist
        - npm install -g pacman-contribution-graph
        # Replace [game-name] with the game you want; repeat for each game
        - pacman-contribution-graph --platform gitlab --username "$CI_PROJECT_NAMESPACE" --game [game-name] --gameTheme gitlab --output dist/[game-name]-contribution-graph.svg
        - pacman-contribution-graph --platform gitlab --username "$CI_PROJECT_NAMESPACE" --game [game-name] --gameTheme gitlab-dark --output dist/[game-name]-contribution-graph-dark.svg
    artifacts:
        paths:
            - dist/*.svg
        expire_in: 1 hour
    rules:
        - if: '$CI_PIPELINE_SOURCE == "schedule"'
        - if: '$CI_PIPELINE_SOURCE == "push"'

deploy_to_readme:
    stage: deploy
    image: alpine:latest
    script:
        - apk add --no-cache git
        - mkdir -p output
        - cp dist/*.svg output/
        - git remote set-url origin https://gitlab-ci-token:${CI_PUSH_TOKEN}@gitlab.com/${CI_PROJECT_PATH}.git
        - git config --global user.email "arcade-bot@example.com"
        - git config --global user.name "Arcade Bot"
        - git add output/*.svg
        - git commit -m "Update arcade contribution graphs [ci skip]" || echo "No changes"
        - git push origin HEAD:main
    rules:
        - if: '$CI_PIPELINE_SOURCE == "schedule"'
        - if: '$CI_PIPELINE_SOURCE == "push"'
Add to Profile README:

In your repository, create or edit the README.md file to include. Replace [USERNAME] with your GitLab username and [game-name] with the game. Repeat the block for each game you enabled.

## My Contribution Graph

<!-- [game-name] -->
<picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://gitlab.com/[USERNAME]/[USERNAME]/-/raw/main/output/[game-name]-contribution-graph-dark.svg">
    <source media="(prefers-color-scheme: light)" srcset="https://gitlab.com/[USERNAME]/[USERNAME]/-/raw/main/output/[game-name]-contribution-graph.svg">
    <img alt="[game-name] contribution graph" src="https://gitlab.com/[USERNAME]/[USERNAME]/-/raw/main/output/[game-name]-contribution-graph.svg">
</picture>
Commit and Push:

Push the changes to GitLab. The Gitlab pipeline will work once, updating the Pac-Man game on your profile.
Schedule pipeline running

Go to your project in GitLab
In the left sidebar, navigate to Build > Pipeline schedules (sometimes under CI/CD > Schedules)
Click New schedule
In the form:
Interval pattern: Enter a cron expression for daily runs. For example, 0 2 \* \* \* to run every day at 2:00 AM (UTC).
Timezone: Select your preferred timezone.
Target branch: Choose the main branch.
Click Save pipeline schedule (or Create pipeline schedule).
Your pacman picture will now be generated automatically every day at the same time.

⏳ Run the Workflow Manually
Once you have everything set up:

Go to the "Actions" tab in your repository
Click "Update Pac-Man Contribution"
Click "Run workflow" > "Run workflow"
This will start the SVG generation process and you will then be able to see the animation working in your README! This implementation will allow your Pac-Man contribution graph to be automatically updated every day, keeping it always up to date with your latest contributions.

🎯 How it Works
The application uses your GitHub contribution data to:

Create a grid where each cell represents a day of contribution
Use the contribution intensity levels provided by the GitHub API:
NONE: Days with no contributions (empty spaces in the game)
FIRST_QUARTILE: Days with few contributions (small points, 1 point in the game)
SECOND_QUARTILE: Days with moderate contributions (medium points, 2 points)
THIRD_QUARTILE: Days with many contributions (large points, 5 points)
FOURTH_QUARTILE: Days with exceptional contributions (power pellets that activate ghost-eating mode)
These levels are relative to each user's contribution pattern and are automatically calculated by GitHub, so the density of elements in the game will reflect each user's unique profile.

Pac-Man navigates the grid using pathfinding algorithms
Ghosts chase Pac-Man with unique behaviors (as in the original game)
All gameplay is recorded and exported as an animated SVG
🤝 Contributing
Contributions are welcome! To contribute:

Fork the repository.
Create a new branch: git checkout -b feature-name.
Make your changes and commit them: git commit -m 'Add feature'.
Push to the branch: git push origin feature-name.
Submit a pull request.
🙏 Acknowledgements
Inspired by the snk project, which turns your GitHub contribution graph into a snake game. Special thanks to all contributors and the open-source community for their support.

🌐 Online tools that use Pac-Man Contribution Graph Game
Profile Readme Generator: Website • Pull Request