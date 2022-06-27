<?php

namespace App\Http\Controllers;
use App\Http\Controllers\Controller;
use Illuminate\Http\Request;
use App\Models\Field_calculate;


class CalculationController extends Controller
{
    public function calculate(Request $request){
        $calc = new Field_calculate();
        if(!$request->get("expression")){
            return response()->json(['message' => 'Expression Not Found!'], 404);
        }
        $exp = $request->get("expression");
        if (!preg_match("#^[0-9 \.\+\-\*\/\(\)]+$#", $exp)) {
            return response()->json(['message' => 'Expression includes unavailable character(s)!'], 404); 
        }
        if (substr_count($exp, '(') != substr_count($exp, ')')) {
            return response()->json(['message' => 'Parenthesis error!'], 404); 
        }
        $res = $calc->calculate($exp);
        $response = response()->json(['result' => $res]);
        return $response;
    }
}
