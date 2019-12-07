const path = require('path');

exports.onCreateWebpackConfig = ({ actions }) => {
  actions.setWebpackConfig({
    resolve: {
      modules: [path.resolve(__dirname, 'src'), 'node_modules'],
    },
  });
};

exports.createPages = async ({ actions, graphql, reporter }) => {
  const result = await graphql(`
    query {
      allMdx {
        nodes {
          frontmatter {
            slug
          }
        }
      }
    }
  `);

  if (result.errors) {
    reporter.panic('failed to create slides', result.errors);
  }

  const slides = result.data.allMdx.nodes;

  slides.forEach(slide => {
    actions.createPage({
      path: slide.frontmatter.slug,
      component: require.resolve('./src/templates/slide.tsx'),
      context: {
        slug: slide.frontmatter.slug,
      },
    });
  });
};
