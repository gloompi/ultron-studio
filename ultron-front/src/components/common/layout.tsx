import React, { FC } from 'react';
import { useStaticQuery, graphql } from 'gatsby';
import { Global, css } from '@emotion/core';

import 'assets/fonts/fonts.css';

import { ThemeProvider, themeInstance } from 'hooks/use-theme';
import Header from 'components/common/header';

const Layout: FC = ({ children }) => {
  const data = useStaticQuery(graphql`
    query SiteTitleQuery {
      site {
        siteMetadata {
          title
        }
      }
    }
  `);

  return (
    <ThemeProvider>
      <Global styles={globalStyles} />
      <Header title={data.site.siteMetadata.title} />
      <main css={mainStyle}>{children}</main>
      <footer css={footerStyle}>
        <div css={themeInstance.container}>
          <div>
            <span>
              © {new Date().getFullYear()} Ultron. All rights reserved by
            </span>
            <a
              href="https://www.linkedin.com/in/gloompi/"
              css={css`
                color: ${themeInstance.colors.primary};
                margin-left: 4px;
              `}
              target="_blank"
            >
              GloompiQue&#x262F;
            </a>
          </div>
        </div>
      </footer>
    </ThemeProvider>
  );
};

const mainStyle = css`
  width: 100%;
  background-color: ${themeInstance.colors.lightBlack};
  min-height: calc(100vh - 50px);
  overflow: hidden;
`;

const footerStyle = css`
  display: flex;
  align-items: center;
  font-family: Hind, sans-serif;
  font-size: 13px;
  width: 100%;
  color: #fff;
  padding: 28px 0;
  background: ${themeInstance.colors.black};
`;

const globalStyles = css`
  * {
    list-style-type: none;
    box-sizing: border-box;
    margin: 0;
    padding: 0;

    &:focus {
      outline: none;
    }
  }

  html,
  body {
    margin: 0;
    color: ${themeInstance.colors.white};
    font-family: Roboto, Helvetica, sans-serif;
    font-size: 18px;

    > div {
      margin-top: 0;
    }

    h1,
    h2,
    h3,
    h4,
    h5,
    h6 {
      color: ${themeInstance.colors.white};
    }

    a {
      text-decoration: none;
    }
  }
`;

export default Layout;
