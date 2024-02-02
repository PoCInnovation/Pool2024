<script>
  import { Route, Router } from 'svelte-routing';
  import Dashboard from './pages/Dashboard.svelte';
  import Home from "./pages/Home.svelte";
  import Login from './pages/Login.svelte';
  import Register from './pages/Register.svelte';

  export const url = "";
</script>

<Router url={url}>
  <Route path="*" component={Home} />
  <Route path="/login" component={Login} />
  <Route path="/register" component={Register} />
  <Route path="/dashboard" component={Dashboard} />
</Router>
