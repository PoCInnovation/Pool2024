<script>
  import Router from "svelte-spa-router";
  import Home from "./pages/Home.svelte";
  import Register from "./pages/Register.svelte";
  import Login from "./pages/Login.svelte";

  let routes = {
      "/": Home,
      "/register": Register,
      "/login": Login,
  }
</script>

<Router {routes} />