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
    <button @click="signup">Sign up</button>
    <button @click="login">Sign in</button>
  </div>
</template>
<script>
import backend from "@/backend/backend";

export default {
  name: "authBox",
  data() {
    return {
      account: '',
    }
  },
  mounted() {
    //get account
    backend.getAccount().then((res) => {
      if (res['status'] === 'ok') {
        console.log("success:", res)
      } else {
        console.log("fail:", res)
      }

    })
  }
  ,
  methods: {
    //get account

    login() {
      window.location.href = this.getSigninUrl();
    },
    signup() {
      window.location.href = this.getSignupUrl();
    },
  }
}
</script>

<style scoped>

</style>
