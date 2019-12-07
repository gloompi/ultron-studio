import React, { FC } from 'react';
import { graphql } from 'gatsby';
import { css } from '@emotion/core';
import { MDXRenderer } from 'gatsby-plugin-mdx';

import Layout from 'components/common/layout';

export const query = graphql`
  query($slug: String) {
    mdx(frontmatter: { slug: { eq: $slug } }) {
      frontmatter {
        slug
        title
        label
      }
      body
    }
  }
`;

interface IProps {
  data: {
    mdx: {
      frontmatter: {
        title: string;
        label: string;
        slug: string;
      };
      body: string;
    };
  };
}

const Slide: FC<IProps> = ({ data: { mdx: slide } }) => {
  return (
    <Layout>
      <h3 css={labelStyles}>{slide.frontmatter.label}</h3>
      <h1>{slide.frontmatter.title}</h1>
      <p>
        <MDXRenderer>{slide.body}</MDXRenderer>
      </p>
    </Layout>
  );
};

const labelStyles = css`
  white-space: nowrap;
  font-size: 22px;
  line-height: 34px;
  font-weight: 300;
  color: #fff;
  text-transform: uppercase;
  letter-spacing: 19px;
`;

export default Slide;
