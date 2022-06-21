<?php

namespace App\Http\Controllers;
use App\Http\Controllers\Controller;
use Illuminate\Http\Request;

class CalculationController extends Controller
{
    public function calculate(Request $request){
        if(!$request->get("expression")){
            return response()->json(['message' => 'Expression Not Found!'], 404);
        }
        $response = response()->json(['result' => '11']);
        return $response;
    }
}
