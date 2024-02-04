<script lang="ts">
    import { Gallery } from "flowbite-svelte";
    import TopBar from "../components/Bar/TopBar.svelte";
    import ArtistCard from "../components/Card/ArtistCard.svelte";
    import type { Artist } from "../types/Artist.svelte";

    let artists:Artist[] = [
        { id: "1",
        name: "Booba",
        rating: 3,
        nationality: "French",
        musicGender: "Rap",
        photoUrl: "https://bit.ly/3U7Oh1D"},
        { id: "2",
        name: "Imagine Dragons",
        rating: 4,
        nationality: "American",
        musicGender: "Pop rock",
        photoUrl: "https://bit.ly/3TSTSsp"},
        ];
    $: displayArtists = artists;
</script>

<TopBar artists={artists}/>
<br/>
<div class="flex justify-center">
    <Gallery class="grid grid-cols-3 gap-4">
        {#each displayArtists as artist (artist.id)}
            <ArtistCard artist={artist}/>
        {/each}
    </Gallery>
</div>
