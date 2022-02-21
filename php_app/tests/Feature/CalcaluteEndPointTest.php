<?php

namespace Tests\Feature;

use Illuminate\Foundation\Testing\RefreshDatabase;
use Illuminate\Foundation\Testing\WithFaker;
use Tests\TestCase;

class CalcaluteEndPointTest extends TestCase
{
    /**
     * A basic feature test example.
     *
     * @return void
     */
    public function test_endpoint_check()
    {
        $response = $this->json('GET', "/calculate", ['expression' => "2+4+5"]);

        $response->assertStatus(200);
    }
    public function test_hasExpressionAttribute()
    {
        $response = $this->json('GET', "/calculate");

        $response->assertStatus(404);
        $this->assertEquals(json_decode($response->getContent())->message, "Expression Not Found!");
    }
    public function test_checkResult(){
        $response = $this->json('GET', "/calculate",['expression' => "2+4+5"]);
        $response->assertStatus(200);
        $this->assertEquals(json_decode($response->getContent())->result, "9");
    }
}
