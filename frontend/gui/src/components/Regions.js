import React from 'react';
import { List } from 'antd';


const Regions = (props) => {
  return(



    <List
      itemLayout="horizontal"
      dataSource={props.data}
      renderItem={item => (
        <List.Item   style={{border: '1px solid rgb(235, 237, 240)', textAlign:'center'}}>
          <List.Item.Meta
            style={{marginLeft:'20px'}}
            title={<a href={`/regions/${item.id}/`}>{item.reg_name}</a>}
            description={"Autoridad Máxima Vigente: " + item.authority}
          />
        </List.Item>
      )}
    />
  )
}

export default Regions;
