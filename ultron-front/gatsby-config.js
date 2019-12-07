const path = require('path');

module.exports = {
  siteMetadata: {
    title: `Ultron Studio`,
    description: `Kick off your next, great project with the best IT team from Middle Asia`,
    author: `gloompi`,
  },
  plugins: [
    {
      resolve: `gatsby-plugin-manifest`,
      options: {
        name: `ultron-studio`,
        short_name: `ultron`,
        start_url: `/`,
        background_color: `#663399`,
        theme_color: `#663399`,
        display: `minimal-ui`,
        icon: `src/assets/images/gatsby-icon.png`,
      },
    },
    'gatsby-plugin-typescript',
    'gatsby-plugin-react-helmet',
    'gatsby-transformer-sharp',
    'gatsby-plugin-sharp',
    'gatsby-plugin-emotion',
    `gatsby-transformer-sharp`,
    `gatsby-plugin-sharp`,
    {
      resolve: 'gatsby-plugin-mdx',
      options: {
        defaultLayouts: {
          default: require.resolve('./src/components/common/layout.tsx'),
        },
      },
    },
    {
      resolve: 'gatsby-source-filesystem',
      options: {
        name: 'images',
        path: path.resolve(__dirname, 'src/assets/images'),
      },
    },
    {
      resolve: 'gatsby-source-filesystem',
      options: {
        name: 'fonts',
        path: path.resolve(__dirname, 'src/assets/fonts'),
      },
    },
    {
      resolve: 'gatsby-source-filesystem',
      options: {
        name: 'slides',
        path: path.resolve(__dirname, 'src/assets/slides'),
      },
    },
    {
      resolve: 'gatsby-source-filesystem',
      options: {
        name: 'deliverables',
        path: path.resolve(__dirname, 'src/assets/deliverables'),
      },
    },
    {
      resolve: 'gatsby-plugin-webpack-bundle-analyzer',
      options: {
        production: true,
        disable: !process.env.ANALYZE_BUNDLE_SIZE,
        generateStatsFile: true,
        analyzerMode: 'static',
      },
    },
  ],
};
