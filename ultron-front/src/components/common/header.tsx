import React, { FC, useState } from 'react';
import { Link } from 'gatsby';
import { css } from '@emotion/core';
import { Waypoint } from 'react-waypoint';

import splitText from 'utils/splitText';
import useTheme, { ITheme } from 'hooks/use-theme';

interface IProps {
  title: string;
}

const Header: FC<IProps> = ({ title }) => {
  const [active, setActive] = useState(false);
  const theme = useTheme();
  const splittedTitle = splitText({ text: title });

  const handleWaypointEnter = () => {
    setActive(false);
  };

  const handleWaypointLeave = () => {
    setActive(true);
  };

  return (
    <>
      <Waypoint
        bottomOffset={70}
        onEnter={handleWaypointEnter}
        onLeave={handleWaypointLeave}
      />
      <header css={headerStyles(theme, active)}>
        <div css={theme.container}>
          <h1 css={h1Styles(theme)}>
            <Link to="/">
              <span>{splittedTitle[0]}</span>
              {splittedTitle[1]}
            </Link>
          </h1>
          <nav>
            <ul css={navListStyles}>
              <li css={navItemStyles(theme)}>
                <Link to="/" activeClassName="active">
                  Home
                </Link>
              </li>
              <li css={navItemStyles(theme)}>
                <Link to="/about" activeClassName="active">
                  About
                </Link>
              </li>
              <li css={navItemStyles(theme)}>
                <Link to="/contacts" activeClassName="active">
                  Contacts
                </Link>
              </li>
            </ul>
          </nav>
        </div>
      </header>
    </>
  );
};

const headerStyles = (theme: ITheme, active: boolean) => css`
  position: fixed;
  display: flex;
  align-items: center;
  justify-content: center;
  top: 0;
  left: 50%;
  height: ${active ? 70 : 120}px;
  width: 100%;
  color: #fff;
  background: ${active ? theme.colors.black : 'transparent'};
  transform: translateX(-50%);
  transition: 0.3s;
  z-index: 1000;
`;

const h1Styles = (theme: ITheme) => css`
  font-family: Hind-Bold, sans-serif;
  font-size: 25px;
  line-height: 1;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: #fff;
  margin: 0;

  & > a {
    color: #fff;
    transition: 0.3s;

    & > span {
      color: ${theme.colors.primary};
    }

    &:hover {
      color: ${theme.colors.primary};
    }
  }
`;

const navListStyles = css`
  display: flex;
  align-items: center;
  justify-content: flex-start;
`;

const navItemStyles = (theme: ITheme) => css`
  letter-spacing: 1.5px;
  margin-right: 36px;

  &:last-child {
    margin-right: 0;
  }

  & > a {
    font-family: Hint-Medium, sans-serif;
    font-size: 14px;
    font-weight: 700;
    color: #fff;
    text-transform: uppercase;
    transition: 0.3s color;

    &.active,
    &:hover {
      color: ${theme.colors.primary};
    }
  }
`;

export default Header;
