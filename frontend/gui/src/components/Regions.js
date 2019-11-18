import React from 'react';
import { List, Avatar } from 'antd';

//import { Link } from 'react-router-dom';



const Regions = (props) => {
  return(



    <List
      itemLayout="horizontal"
      dataSource={props.data}
      renderItem={item => (
        <List.Item   style={{border: '1px solid rgb(235, 237, 240)', textAlign:'center'}}>
          <List.Item.Meta
            style={{marginLeft:'20px'}}
            // title={<Link to={"/" + item.id}>{item.reg_name}</Link>}
            title={<a href={`/regions/${item.id}`}>{item.reg_name}</a>}
            description={"Autoridad Máxima Vigente: " + item.authority}
          />
        </List.Item>
      )}
    />
  )
}

export default Regions;
