<script>
    import { push } from "svelte-spa-router";
    
    let email = "";
    let password = "";
    let confirmedPassword = "";

    const userRegistered = () => {
        console.log("Email", email);
        console.log("Password", password);
        console.log("Confirmed password", confirmedPassword);
    }

    const goToLogin = () => {
        push("/login");
    }
</script>

<h1>Register</h1>
<input type="email" placeholder="Email" bind:value={email}>
<input type="password" placeholder="Password" bind:value={password}>
<input type="password" placeholder="Confirm password" bind:value={confirmedPassword}>
<button on:click={userRegistered}>Register</button>
<button on:click={goToLogin}>Already a user ? Login</button>