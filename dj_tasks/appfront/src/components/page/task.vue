<template>
  <div>
 <div class="table">
        <!--<div class="crumbs">-->
            <!--<el-breadcrumb separator="/">-->
                <!--<el-breadcrumb-item><i class="el-icon-menu"></i> 表格</el-breadcrumb-item>-->
                <!--<el-breadcrumb-item>基础表格</el-breadcrumb-item>-->
            <!--</el-breadcrumb>-->
        <!--</div>-->
        <!--<div class="handle-box">-->
            <!--<el-button type="primary" icon="delete" class="handle-del mr10" @click="delAll">批量删除</el-button>-->
            <!--<el-select v-model="select_cate" placeholder="筛选省份" class="handle-select mr10">-->
                <!--<el-option key="1" label="广东省" value="广东省"></el-option>-->
                <!--<el-option key="2" label="湖南省" value="湖南省"></el-option>-->
            <!--</el-select>-->
            <!--<el-input v-model="select_word" placeholder="筛选关键词" class="handle-input mr10"></el-input>-->
            <!--<el-button type="primary" icon="search" @click="search">搜索</el-button>-->
        <!--</div>-->
        <el-table :data="tableData" border style="width: 100%" ref="multipleTable" @selection-change="handleSelectionChange">
            <!--<el-table-column type="selection" width="55"></el-table-column>-->
              <el-table-column
                label="日期"
                width="180">
                <template slot-scope="scope">
                  <i class="el-icon-time"></i>
                  <span style="margin-left: 10px">{{ scope.row.date }}</span>
                </template>
              </el-table-column>
            <el-table-column prop="fields.owner" label="日期" sortable width="150">
            </el-table-column>
            <el-table-column prop="fields.name" label="姓名" width="120">
            </el-table-column>
            <el-table-column prop="fields.body" label="地址" :formatter="formatter">
            </el-table-column>
            <!--<el-table-column label="操作" width="180">-->
                <!--<template scope="scope">-->
                    <!--<el-button size="small"-->
                            <!--@click="handleEdit(scope.$index, scope.row)">编辑</el-button>-->
                    <!--<el-button size="small" type="danger"-->
                            <!--@click="handleDelete(scope.$index, scope.row)">删除</el-button>-->
                <!--</template>-->
            <!--</el-table-column>-->
        </el-table>
        <div class="pagination">
            <el-pagination
                    @current-change ="handleCurrentChange"
                    layout="prev, pager, next"
                    :total="1000">
            </el-pagination>
        </div>
    </div>
</div>
</template>

<script>
    export default {
      // data: function(){
      //       return {}
      //   }
        data() {
            return {
                url: './static/vuetable.json',
                tableData: [],
                cur_page: 1,
                multipleSelection: [],
                select_cate: '',
                select_word: '',
                del_list: [],
                is_search: false
            }
        },
        created(){
            this.getData();
        },
        // computed: {
        //       data(){
        //           const self = this;
        //           return self.tableData.filter(function(d){
        //               let is_del = false;
        //               for (let i = 0; i < self.del_list.length; i++) {
        //                   if(d.name === self.del_list[i].name){
        //                       is_del = true;
        //                       break;
        //                   }
        //               }
        //               if(!is_del){
        //                   if(d.address.indexOf(self.select_cate) > -1 &&
        //                       (d.name.indexOf(self.select_word) > -1 ||
        //                       d.address.indexOf(self.select_word) > -1)
        //                   ){
        //                       return d;
        //                   }
        //               }
        //           })
        //       }
        //   },
        methods: {
              handleCurrentChange(val){
                  this.cur_page = val;
                  this.getData();
              },
              showBooks(res){
                this.tableData = res.body;
                console.log('tableData:', this.tableData)
              },
              getData(){
                  let self = this;
                  self.tableData = [];
                  self.url = '/tasks/';
                  console.log('url:', self.url);
                  this.$http.get('http://127.0.0.1:8000/tasks/')
                    .then((response) => {
                        // console.log('response:', response);
                        // let res = JSON.parse(response.bodyText);

                        if (response.error) {
                          this.$message.error('新增书籍失败，请重试');
                          console.log(res['msg'])
                        } else {
                            console.log('body:', response.body);
                            this.showBooks(response)
                        }
                    })
                  // self.$axios.get(self.url).then((res) => {
                  //     console.log('res:', res);
                  //     self.tableData = res.data.list;
                  // })
                  // self.$axios.post(self.url, {page:self.cur_page}).then((res) => {
                  //     console.log('res:', res);
                  //     self.tableData = res.data.list;
                  // })
              },
              search(){
                  this.is_search = true;
              },
              formatter(row, column) {
                  return row.address;
              },
              filterTag(value, row) {
                  return row.tag === value;
              },
              handleEdit(index, row) {
                  this.$message('编辑第'+(index+1)+'行');
              },
              handleDelete(index, row) {
                  this.$message.error('删除第'+(index+1)+'行');
              },
              delAll(){
                  const self = this,
                      length = self.multipleSelection.length;
                  let str = '';
                  self.del_list = self.del_list.concat(self.multipleSelection);
                  for (let i = 0; i < length; i++) {
                      str += self.multipleSelection[i].name + ' ';
                  }
                  self.$message.error('删除了'+str);
                  self.multipleSelection = [];
              },
              handleSelectionChange(val) {
                  this.multipleSelection = val;
              }
          }
    }
</script>
