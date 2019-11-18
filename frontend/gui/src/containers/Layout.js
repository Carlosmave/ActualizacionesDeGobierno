import React from 'react';


import { Layout, Menu, Breadcrumb } from 'antd';
import { Link } from 'react-router-dom';

const { Header, Content, Footer } = Layout;

const CustomLayout = (props) => {
    return(
      <Layout className="layout">
        <Header>
          <div className="logo" />
          <Menu
            theme="dark"
            mode="horizontal"
            defaultSelectedKeys={['1']}
            style={{ lineHeight: '64px' }}
          >
            <Menu.Item key="1"><a href='/'>Actualizaciones de Gobierno</a></Menu.Item>
          </Menu>
        </Header>
        <Content style={{ padding: '0 50px' }}>
          <Breadcrumb style={{ margin: '16px 0' }}>

          </Breadcrumb>
            <div style={{ background: '#fff', padding: 24, minHeight: 280 }}>
              {props.children}
            </div>
        </Content>
        <Footer style={{ textAlign: 'center' }}>© 2019 Carlos Martinez</Footer>
      </Layout>
    );
}

export default CustomLayout;
