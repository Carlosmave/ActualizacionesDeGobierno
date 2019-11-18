import React from 'react';
import { List } from 'antd';



const Politicians = (props) => {
  return(
    <List
      itemLayout="horizontal"
      dataSource={props.data}
      renderItem={item => (
        <List.Item style={{border: '1px solid rgb(235, 237, 240)', textAlign:'center'}}>
          <List.Item.Meta
            style={{marginLeft:'20px'}}
            title={<a href={`/politicians/${item.id}/`}>{item.poli_name}</a>}
            description={"Puesto: " + item.job}
          />
        </List.Item>
      )}
    />
  )
}

export default Politicians;
