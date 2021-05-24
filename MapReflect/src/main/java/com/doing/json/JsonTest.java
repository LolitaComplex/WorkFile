package com.doing.json;

import com.google.gson.Gson;

import java.util.ArrayList;

public class JsonTest {

    public static void main(String[] args) {

        TestArrayList list = new TestArrayList();
        list.add("123");

        String json =  new Gson().toJson(list);

        System.out.println(json);
    }
}
