import React from 'react';
import MainHeader from '../../components/headers/mainHeader'
import MainFooter from '../../components/headers/mainFooter'

import './style.css'

const MainLayout = ({ children }) => {
  return (
    <div id='MainLayout'>
      <MainHeader />
        {children}
      <MainFooter />
    </div>
  );
};

export default MainLayout;