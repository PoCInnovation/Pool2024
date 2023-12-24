<script>
    import { push } from "svelte-spa-router";

    const goToLogin = () => {
        push("/login");
    }

    const goToRegister = () => {
        push("/register");
    }
</script>

<h1>Artists Book</h1>
<h2>Manage your favorite artists</h2>
<button on:click={goToLogin}>Login</button>
<button on:click={goToRegister}>Register</button>