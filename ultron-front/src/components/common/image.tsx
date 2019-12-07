import React, { FC } from 'react';
import Img from 'gatsby-image';
import { useStaticQuery, graphql } from 'gatsby';

interface IProps {
  imageName: string;
}

const Image: FC<IProps> = () => {
  const data = useStaticQuery(graphql`
    query {
      placeholderImage: file(relativePath: { eq: ".png" }) {
        childImageSharp {
          fluid(maxWidth: 300) {
            ...GatsbyImageSharpFluid
          }
        }
      }
    }
  `);

  return <Img fluid={data.placeholderImage.childImageSharp.fluid} />;
};

export default Image;
