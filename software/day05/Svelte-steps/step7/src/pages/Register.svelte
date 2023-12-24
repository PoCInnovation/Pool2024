<script>
    import { Button, Heading, Input } from "flowbite-svelte";
    import { push } from "svelte-spa-router";
    
    let email = "";
    let password = "";
    let confirmedPassword = "";

    const userRegistered = () => {
        console.log("Email", email);
        console.log("Password", password);
        console.log("Confirmed password", confirmedPassword);
        push("/dashboard");
    }

    const goToLogin = () => {
        push("/login");
    }
</script>

<Heading tag="h1" class="text-center">Register</Heading>
<br/>
<Input type="email" placeholder="Email" bind:value={email}/>
<Input type="password" placeholder="Password" bind:value={password}/>
<Input type="password" placeholder="Confirm password" bind:value={confirmedPassword}/>
<br/>
<Button on:click={userRegistered}>Register</Button>
<Button on:click={goToLogin}>Already a user ? Login</Button>
