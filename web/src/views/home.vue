<!--Copyright 2022 The Casdoor Authors. All Rights Reserved.-->

<!--Licensed under the Apache License, Version 2.0 (the "License");-->
<!--you may not use this file except in compliance with the License.-->
<!--You may obtain a copy of the License at-->

<!--     http://www.apache.org/licenses/LICENSE-2.0-->

<!--Unless required by applicable law or agreed to in writing, software-->
<!--distributed under the License is distributed on an "AS IS" BASIS,-->
<!--WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.-->
<!--See the License for the specific language governing permissions and-->
<!--limitations under the License.-->

<template>
  <div>
    <div>
      <table border="1">
        <tr>
          <th>Name</th>
          <th>Value</th>
        </tr>
        <tr>
          <td>user name</td>
          <td>{{ account.name }}</td>
        </tr>
        <tr>
          <td>user avatar</td>
          <td><img :src="account.avatar" alt="user avatar" style="width:50px"/></td>
        </tr>
        <tr>
          <td>user id</td>
          <td>{{ account.id }}</td>
        </tr>
        <tr>
          <td>user owner</td>
          <td>{{ account.owner }}</td>
        </tr>
        <tr>
          <td>user created time</td>
          <td>{{ account.createdTime }}</td>
        </tr>
      </table>
    </div>
    <br>
    <button @click="logout">Sign out</button>
  </div>
</template>

<script>
import backend from "@/backend/backend";

export default {
  name: "homePage",
  data() {
    return {
      account: "",
      userUrl: "",
    };
  },
  mounted() {
    backend.getAccount().then((res) => {
      if (res['status'] === 'ok') {
        this.account = res['data']
        console.log("success:", this.account)
      } else {
        console.log("fail:", res)
      }
    });
  },
  methods: {
    logout() {
      backend.logOut().then((res) => {
        if (res['status'] === 'ok') {
          console.log("success:", res)
        } else {
          console.log("fail:", res)
        }
        window.location.href = "/";
      });
    }
  }
}
</script>

<style scoped>

</style>
