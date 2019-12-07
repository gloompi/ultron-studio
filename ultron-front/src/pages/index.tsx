import React, { FC } from 'react';

import Layout from 'components/common/layout';
import SEO from 'components/common/seo';
import Section1 from 'components/home/section-1';
import Section2 from 'components/home/section-2';
import Section3 from 'components/home/section-3';
import Section4 from 'components/home/section-4';
import Section5 from 'components/home/section-5';
import Section6 from 'components/home/section-6';
import Section7 from 'components/home/section-7';
import Section8 from 'components/home/section-8';
import Section9 from 'components/home/section-9';
import Section10 from 'components/home/section-10';

const IndexPage: FC = () => (
  <Layout>
    <SEO title="Home" />
    <Section1 />
    <Section2 />
    <Section3 />
    <Section4 />
    <Section5 />
    <Section6 />
    <Section7 />
    <Section8 />
    <Section9 />
    <Section10 />
  </Layout>
);

export default IndexPage;
