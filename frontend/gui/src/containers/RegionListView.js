import React from 'react';
import axios from 'axios';
import { Input, PageHeader } from 'antd';

import Regions from '../components/Regions';


class RegionList extends React.Component {

    state = {
      search: "",
      regions:[]
    }

    componentDidMount() {
      axios.get('http://127.0.0.1:8000/regions/')
          .then(res => {
              this.setState({
                regions: res.data
              });
              console.log(res.data);
          })
    }


    onChange = e => {
      this.setState({ search: e.target.value });
    };

  render() {
    const search = this.state.search;
    const filteredRegions = this.state.regions.filter(region => {
      return region.reg_name.toLowerCase().indexOf(search.toLowerCase()) !== -1;
    });
    const { Search } = Input;
    return(
      <div>
      <PageHeader
        style={{
          border: '1px solid rgb(235, 237, 240)',
        }}
        title="Regiones"
      />
      <br />
      <Search
        placeholder="Buscar región"
        onChange={this.onChange}
      />
      <br />
      <br />
      <Regions data={filteredRegions} />
      </div>
    )
  }
}

export default RegionList

// <Input
//   label="Search Region"
//   icon="search"
//   onChange={this.onChange}
// />
    // renderRegion = region => {
    //   const { search } = this.state;
    //   var name = region.reg_name.toLowerCase();
    //
    //   return (
    //     <div className="col-md-3" style={{ marginTop: "20px" }}>
    //       <Card>
    //           <p className="">
    //           </p>
    //           <p title={region.reg_name}></p>
    //             <p>{region.reg_name.substring(0, 15)}</p>
    //             <p>{region.reg_name.length > 15 && "..."}</p>
    //       </Card>
    //     </div>
    //   );
    // };

// render() {
//   const { search } = this.state;
//   const filteredRegions = this.state.regions.filter(region => {
//     return region.reg_name.toLowerCase().indexOf(search.toLowerCase()) !== -1;
//   });
//
//   return (
//     <div className="flyout">
//       <main style={{ marginTop: "4rem" }}>
//         <div className="container">
//           <div className="row">
//             <div className="col-12">
//             </div>
//             <div className="col">
//               <Input
//                 label="Search Region"
//                 icon="search"
//                 onChange={this.onchange}
//               />
//             </div>
//             <div className="col" />
//           </div>
//           <div className="row"> ssss
//             {filteredRegions.map(region => {
//               return this.renderRegion(region);
//             })}
//             aaaa
//           </div>
//         </div>
//       </main>
//     </div>
//   );
// }
